# Problem Description
This project focuses on **AI-Powered Safe Route Optimization for Women and Solo Travelers**. Traditional navigation apps typically optimize for distance or time, which might lead users through poorly lit, high-crime, or deserted areas, especially at night. This OpenEnv-compatible environment simulates a real-world scenario where an AI agent acts to choose the safest possible route between a source and destination by evaluating multiple dynamic safety factors.

# Explanation of Environment
The `SafeRouteEnv` is a custom RL environment built for evaluating different safe-routing policies. Each step consists of an agent being presented with a time of day and a list of alternative routes, from which it must select the most appropriate one.

### State Space
The state is a dictionary representing the current context, including:
- `time_of_day`: A string which can be either `"day"` or `"night"`.
- `routes`: A list of exactly 3 available routes.

Each route contains:
- `crime_rate`: Float from 0.0 to 1.0 (lower is better).
- `lighting_level`: Float from 0.0 to 1.0 (higher is better).
- `crowd_density`: Float from 0.0 to 1.0 (balanced ~0.5 is best, avoiding completely deserted or dangerously overcrowded areas).
- `distance`: Numeric float representing the length of the route.
- `dynamic_risk`: Float from 0.0 to 1.0, representing suddenly occurring risks, which can increase randomly or during nighttime.

### Action Space
Discrete string choice of route:
`["route_1", "route_2", "route_3"]`

### Reward Logic
The reward function yields a continuous value between `0.0` and `1.0`.
- **Higher reward** for: routes with low crime, good lighting, and balanced crowds.
- **Penalties** are applied for: unsafe features (like high dynamic risk or high crime rates).
- **Distance Penalty**: A small penalty is applied for excessively long routes to ensure efficiency isn't completely ignored.
- **Partial Rewards**: Are assigned for sub-optimal but reasonably safe routes.

### Task Descriptions
The environment includes three difficulty modules to assess policies:
- **Easy Task**: Choose the route strictly based on the lowest `crime_rate`.
- **Medium Task**: Balance multiple safety factors by considering `crime_rate`, `lighting_level`, and `crowd_density`.
- **Hard Task**: Make comprehensive trade-offs optimizing overall safety, dynamic risk, distance, and time context.

---

# Setup Instructions and Execution

### Local Python Setup
1. Clone the repository and navigate to the root directory.
2. Ensure you have Python 3.10+ installed.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run inference:
   ```bash
   python inference.py
   ```

### Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t safe-route-env .
   ```
2. Run the environment:
   ```bash
   docker run --rm safe-route-env
   ```
