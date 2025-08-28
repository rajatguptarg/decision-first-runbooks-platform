"""Models for execution environment."""

from pydantic import BaseModel, Field


class ResourceLimits(BaseModel):
    """Container resource limits."""

    memory_mb: int = 512
    cpu_limit: float = 1.0
    timeout_seconds: int = 3600


class VolumeMount(BaseModel):
    """Container volume mount configuration."""

    host_path: str
    container_path: str
    read_only: bool = False


class ExecutionEnvironment(BaseModel):
    """Defines a containerized execution environment for a runbook."""

    name: str
    base_image: str
    dockerfile_content: str | None = None
    environment_variables: dict[str, str] = Field(default_factory=dict)
    volumes: list[VolumeMount] = Field(default_factory=list)
    network_mode: str = "bridge"
    resource_limits: ResourceLimits = Field(default_factory=ResourceLimits)
