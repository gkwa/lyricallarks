# OpenTelemetry Hello World Demo

A modularized example showing how to add OpenTelemetry to Python code without making it noisy.

## Structure
```
.
├── pyproject.toml         # Project dependencies (uv)
├── telemetry.py          # All OpenTelemetry setup (isolated here!)
├── greeter.py            # Business logic (clean and focused)
├── greeter_decorator.py  # Alternative decorator approach
└── main.py               # Application entry point
```

## Key Design Principles

1. **Separation of Concerns**: All OpenTelemetry setup is in `telemetry.py`
2. **Absolute Imports**: Uses `import module` pattern for consistency
3. **Decorator Pattern**: Use `@traced()` for clean instrumentation
4. **No Noise**: Business logic remains readable and focused
5. **Easy to Remove**: Can disable telemetry by not initializing it

## Installation

Using [uv](https://github.com/astral-sh/uv):
```bash
uv sync
```

Or with pip:
```bash
pip install -e .
```

## Running
```bash
uv run python main.py
```

Or:
```bash
python main.py
```

You'll see:
- Your application output
- Trace spans printed to console (for demo purposes)

## In Production

Replace `ConsoleSpanExporter` in `telemetry.py` with:
```python
import opentelemetry.exporter.otlp.proto.grpc.trace_exporter

# Send to your observability backend (Jaeger, Honeycomb, etc.)
otlp_exporter = opentelemetry.exporter.otlp.proto.grpc.trace_exporter.OTLPSpanExporter(
    endpoint="http://your-collector:4317"
)
provider.add_span_processor(
    opentelemetry.sdk.trace.export.BatchSpanProcessor(otlp_exporter)
)
```

## Benefits of This Approach

- ✅ Business logic stays clean
- ✅ Telemetry can be turned on/off easily
- ✅ Consistent instrumentation patterns
- ✅ Easy to test (mock the telemetry module)
- ✅ Scales well as your codebase grows
- ✅ Absolute imports for clarity
