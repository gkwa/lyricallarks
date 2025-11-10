"""
Business logic - notice how clean this is!
Telemetry is present but not intrusive.
"""

import telemetry


def greet(name: str) -> str:
    """Simple greeting function - traced automatically."""
    t = telemetry.get_telemetry()

    with t.tracer.start_as_current_span("greeter.greet"):
        t.set_attribute("user.name", name)
        t.add_event("Generating greeting")

        greeting = f"Hello, {name}!"
        return greeting


def process_greeting(name: str) -> dict:
    """
    Process a greeting request.
    This demonstrates nested spans.
    """
    t = telemetry.get_telemetry()

    with t.tracer.start_as_current_span("greeter.process_greeting"):
        t.add_event("Starting greeting processing")

        # This call creates a child span automatically
        message = greet(name)

        result = {"message": message, "length": len(message), "processed": True}

        t.set_attribute("result.length", result["length"])
        return result
