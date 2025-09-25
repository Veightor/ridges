"""
Repository cloning utilities for sandbox operations.
"""

import os
import subprocess
import tempfile
import shutil
from pathlib import Path


def clone_repo(target_dir: Path, repo_url: str, base_commit: str) -> None:
    """
    Clone a repository to a target directory at a specific commit.
    
    Args:
        target_dir: Directory to clone the repository into
        repo_url: Repository URL or identifier
        base_commit: Commit hash to checkout
        
    Raises:
        RuntimeError: If the clone operation fails
    """
    try:
        # Ensure target directory exists
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # For SWE-bench, repo_url might be in format "owner/repo"
        # Convert to GitHub URL if needed
        if "/" in repo_url and not repo_url.startswith(("http://", "https://", "git@")):
            git_url = f"https://github.com/{repo_url}.git"
        else:
            git_url = repo_url
        
        # Clone with shallow fetch to save space and time
        clone_cmd = [
            "git", "clone", "--depth", "1", 
            "--no-single-branch", git_url, str(target_dir)
        ]
        
        result = subprocess.run(
            clone_cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Fetch the specific commit if it's not in the shallow clone
        fetch_cmd = ["git", "fetch", "origin", base_commit]
        subprocess.run(
            fetch_cmd,
            cwd=target_dir,
            capture_output=True,
            text=True,
            check=False  # Don't fail if commit is already available
        )
        
        # Checkout the specific commit
        checkout_cmd = ["git", "checkout", base_commit]
        result = subprocess.run(
            checkout_cmd,
            cwd=target_dir,
            capture_output=True,
            text=True,
            check=True
        )
        
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to clone repository {repo_url} at commit {base_commit}: {e.stderr}")
    except Exception as e:
        raise RuntimeError(f"Failed to clone repository {repo_url}: {str(e)}")
