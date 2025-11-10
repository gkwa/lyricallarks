"""
Main application - demonstrates clean separation of concerns.
Telemetry is initialized once and then business logic stays clean.
"""

import telemetry
import greeter


def main():
    # Initialize telemetry once at application startup
    _ = telemetry.init_telemetry(
        service_name="hello-world-service", service_version="1.0.0"
    )

    print("=" * 60)
    print("OpenTelemetry Hello World Demo")
    print("=" * 60)
    print()

    # Business logic - clean and focused
    result = greeter.process_greeting("World")
    print(f"Result: {result['message']}")
    print()

    result = greeter.process_greeting("OpenTelemetry")
    print(f"Result: {result['message']}")
    print()

    print("=" * 60)
    print("Trace output appears above/below")
    print("=" * 60)


if __name__ == "__main__":
    main()
