"""
Telemetry module - encapsulates all OpenTelemetry setup.
This keeps observability concerns separate from business logic.
"""

import functools
import typing
import opentelemetry.trace
import opentelemetry.sdk.trace
import opentelemetry.sdk.trace.export
import opentelemetry.sdk.resources


class Telemetry:
    """Handles OpenTelemetry initialization and provides clean instrumentation helpers."""

    def __init__(self, service_name: str, service_version: str = "1.0.0"):
        """Initialize telemetry for the service."""
        # Create resource with service information
        resource = opentelemetry.sdk.resources.Resource.create(
            {
                "service.name": service_name,
                "service.version": service_version,
            }
        )

        # Set up tracer provider
        provider = opentelemetry.sdk.trace.TracerProvider(resource=resource)

        # Add console exporter for demo purposes
        # In production, you'd use OTLP exporter to send to a backend
        console_exporter = opentelemetry.sdk.trace.export.ConsoleSpanExporter()
        provider.add_span_processor(
            opentelemetry.sdk.trace.export.BatchSpanProcessor(console_exporter)
        )

        # Set as global tracer provider
        opentelemetry.trace.set_tracer_provider(provider)

        # Get tracer for this service
        self.tracer = opentelemetry.trace.get_tracer(service_name, service_version)

    def trace_function(self, span_name: typing.Optional[str] = None):
        """
        Decorator to trace a function.

        Usage:
            @telemetry.trace_function()
            def my_function():
                pass
        """

        def decorator(func: typing.Callable) -> typing.Callable:
            name = span_name or f"{func.__module__}.{func.__name__}"

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                with self.tracer.start_as_current_span(name):
                    return func(*args, **kwargs)

            return wrapper

        return decorator

    def add_event(self, message: str, attributes: typing.Optional[dict] = None):
        """Add an event to the current span."""
        span = opentelemetry.trace.get_current_span()
        if span:
            span.add_event(message, attributes or {})

    def set_attribute(self, key: str, value):
        """Set an attribute on the current span."""
        span = opentelemetry.trace.get_current_span()
        if span:
            span.set_attribute(key, value)


# Global telemetry instance (initialized by the application)
_telemetry: typing.Optional[Telemetry] = None


def init_telemetry(service_name: str, service_version: str = "1.0.0") -> Telemetry:
    """Initialize global telemetry instance."""
    global _telemetry
    _telemetry = Telemetry(service_name, service_version)
    return _telemetry


def get_telemetry() -> Telemetry:
    """Get the global telemetry instance."""
    if _telemetry is None:
        raise RuntimeError("Telemetry not initialized. Call init_telemetry() first.")
    return _telemetry
