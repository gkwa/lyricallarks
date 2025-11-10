"""
Alternative approach using a decorator factory.
This version is even cleaner at the call site.
"""

import functools
import typing
import telemetry


def traced(span_name: typing.Optional[str] = None):
    """
    Decorator that adds tracing to a function.

    Usage:
        @traced()
        def my_function():
            pass

    Or with custom span name:
        @traced("custom.span.name")
        def my_function():
            pass
    """

    def decorator(func: typing.Callable) -> typing.Callable:
        name = span_name or f"{func.__module__}.{func.__name__}"

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            t = telemetry.get_telemetry()
            with t.tracer.start_as_current_span(name):
                return func(*args, **kwargs)

        return wrapper

    return decorator


# Now your business logic is even cleaner:


@traced()
def greet_v2(name: str) -> str:
    """Greeting with decorator - super clean!"""
    t = telemetry.get_telemetry()
    t.set_attribute("user.name", name)
    t.add_event("Generating greeting")
    return f"Hello, {name}!"


@traced("custom.greeting.processor")
def process_greeting_v2(name: str) -> dict:
    """Process greeting with custom span name."""
    t = telemetry.get_telemetry()
    t.add_event("Starting processing")

    message = greet_v2(name)

    result = {"message": message, "length": len(message), "processed": True}

    t.set_attribute("result.length", result["length"])
    return result


if __name__ == "__main__":
    # Initialize telemetry
    telemetry.init_telemetry("hello-world-service", "1.0.0")

    # Use the functions
    print("\n=== Decorator-based approach ===")
    result = process_greeting_v2("OpenTelemetry")
    print(f"Result: {result['message']}")
    print()
