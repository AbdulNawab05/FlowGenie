def generate_flowchart(text):
    user_text = text.lower().strip()

    # Predefined chatbot-like understanding for common problems
    if "even" in user_text and "odd" in user_text:
        return """flowchart TD
A([Start]) --> B[/Input Number/]
B --> C{Is number % 2 == 0?}
C -->|Yes| D[Display Even]
C -->|No| E[Display Odd]
D --> F([End])
E --> F
"""

    elif "positive" in user_text and "negative" in user_text:
        return """flowchart TD
A([Start]) --> B[/Input Number/]
B --> C{Is number >= 0?}
C -->|Yes| D[Display Positive]
C -->|No| E[Display Negative]
D --> F([End])
E --> F
"""

    elif "largest" in user_text and ("three" in user_text or "3" in user_text):
        return """flowchart TD
A([Start]) --> B[/Input three numbers a, b, c/]
B --> C{Is a > b and a > c?}
C -->|Yes| D[Display a is largest]
C -->|No| E{Is b > c?}
E -->|Yes| F[Display b is largest]
E -->|No| G[Display c is largest]
D --> H([End])
F --> H
G --> H
"""

    elif "factorial" in user_text:
        return """flowchart TD
A([Start]) --> B[/Input Number n/]
B --> C[Set fact = 1, i = 1]
C --> D{i <= n?}
D -->|Yes| E[fact = fact * i]
E --> F[i = i + 1]
F --> D
D -->|No| G[Display fact]
G --> H([End])
"""

    elif "sum" in user_text and "natural" in user_text:
        return """flowchart TD
A([Start]) --> B[/Input Number n/]
B --> C[Set sum = 0, i = 1]
C --> D{i <= n?}
D -->|Yes| E[sum = sum + i]
E --> F[i = i + 1]
F --> D
D -->|No| G[Display sum]
G --> H([End])
"""

    elif "prime" in user_text:
        return """flowchart TD
A([Start]) --> B[/Input Number n/]
B --> C{Is n <= 1?}
C -->|Yes| D[Display Not Prime]
C -->|No| E[Set i = 2]
E --> F{i < n?}
F -->|Yes| G{Is n % i == 0?}
G -->|Yes| D
G -->|No| H[i = i + 1]
H --> F
F -->|No| I[Display Prime]
D --> J([End])
I --> J
"""

    # Fallback generic flowchart
    else:
        return f"""flowchart TD
A([Start]) --> B[Understand User Input]
B --> C[Process: {text}]
C --> D[Generate Flowchart]
D --> E([End])
"""