"""
Schema definitions for sandbox operations.
"""

from typing import Optional
from uuid import UUID
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class SandboxStatus(Enum):
    """Status of a sandbox evaluation run."""
    started = "started"
    sandbox_created = "sandbox_created"
    patch_generated = "patch_generated"
    eval_started = "eval_started"
    result_scored = "result_scored"
    cancelled = "cancelled"


class SandboxInput(BaseModel):
    """Input data structure for sandbox operations."""
    instance_id: str
    problem_statement: str
    repo: str
    base_commit: str
    test_patch: str
    run_id: UUID


class SwebenchProblem(BaseModel):
    """Represents a problem from the SWE-bench dataset."""
    instance_id: str
    problem_statement: str
    repo: str
    base_commit: str
    test_patch: str


class EvaluationRun(BaseModel):
    """Represents an evaluation run for a specific problem."""
    run_id: UUID
    evaluation_id: Optional[UUID] = None
    swebench_instance_id: str
    response: Optional[str] = None
    error: Optional[str] = None
    pass_to_fail_success: Optional[str] = None
    fail_to_pass_success: Optional[str] = None
    pass_to_pass_success: Optional[str] = None
    fail_to_fail_success: Optional[str] = None
    solved: Optional[bool] = None
    status: SandboxStatus
    started_at: datetime
    sandbox_created_at: Optional[datetime] = None
    patch_generated_at: Optional[datetime] = None
    eval_started_at: Optional[datetime] = None
    result_scored_at: Optional[datetime] = None
    cancelled_at: Optional[datetime] = None
    logs: Optional[str] = None
