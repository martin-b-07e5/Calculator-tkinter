"""Mathematical expression parsing and processing"""

import re


def parse_expression(expression):
    """Parses and normalizes mathematical expressions"""
    if not expression or expression.strip() == "":
        raise ValueError("Empty expression")

    # Clean spaces
    expression = expression.strip()

    # Replace alternative notations
    expression = expression.replace("×", "*").replace("÷", "/")

    # Replace ^ operator with power function calls
    expression = _replace_power_operator(expression)

    # Validate allowed characters (updated to include power() function)
    valid_chars = r"^[0-9+\-*/().\s^%!eEa-zA-Z_,]+$"
    if not re.match(valid_chars, expression):
        raise ValueError("Invalid characters in expression")

    return expression


def _replace_power_operator(expression):
    """Replaces ^ operator with power function calls"""
    # Pattern to find any valid expression before and after ^
    # This handles: numbers, variables, parenthesized expressions
    # pattern = r"([0-9]+(?:\.[0-9]+)?|\([^)]+\)|[a-zA-Z_][a-zA-Z0-9_]*)\s*\^\s*([0-9]+(?:\.[0-9]+)?|\([^)]+\)|[a-zA-Z_][a-zA-Z0-9_]*)"
    # pattern = r"(\d+(?:\.\d+)?|\([^)]+\)|[a-zA-Z_]\w*)\s*\^\s*(\d+(?:\.\d+)?|\([^)]+\)|[a-zA-Z_]\w*)"
    # Factor the repeated alternative into a single 'atom' subpattern for clarity.
    # The atom matches: numbers (integers or decimals), parenthesized expressions, or identifiers.
    # Note: this keeps the original behaviour (no scientific notation, no nested-parenthesis parsing).
    atom = r"(?:\d+(?:\.\d+)?|\([^)]+\)|[a-zA-Z_]\w*)"
    pattern = rf"({atom})\s*\^\s*({atom})"

    def replace_match(match):
        base = match.group(1)
        exponent = match.group(2)
        return f"power({base}, {exponent})"

    # Apply replacement until no more ^ operators are found
    while "^" in expression:
        new_expression = re.sub(pattern, replace_match, expression)
        if new_expression == expression:  # No changes made
            break
        expression = new_expression

    return expression


""" ### 1. Definición del patrón `atom`

```python
atom = r"(?:\d+(?:\.\d+)?|\([^)]+\)|[a-zA-Z_]\w*)"
```

- **`(?: ... )`**: Este es un grupo de no captura. Se utiliza cuando deseas agrupar partes de una expresión regular, pero no necesitas almacenar esa parte como un grupo separado para referencias posteriores.
- **`|\([^)]+\)`**: Este es un patrón que captura cualquier expresión entre paréntesis. `[^)]+` significa "cualquier carácter que no sea un paréntesis de cierre". Esto asegura que solo se capture el contenido dentro de los paréntesis.
- **`[a-zA-Z_]\w*`**: Captura identificadores que empiezan con una letra (mayúscula o minúscula) o un guion bajo, seguido de cero o más caracteres alfanuméricos o guiones bajos. Esto asegura que las variables o nombres sean válidos.

Entonces, el patrón `atom` asegura que puedes capturar:
- Números enteros y decimales (`\d+(?:\.\d+)?`)
- Expresiones entre paréntesis
- Identificadores de variables

### 2. Uso del patrón `atom` en `pattern`

```python
pattern = rf"({atom})\s*\^\s*({atom})"
```

Aquí estás utilizando el `atom` en un nuevo patrón denominado `pattern`.

- **`rf"(...)"`**: Esto es un "raw f-string", que permite definir la cadena como literal (sin procesar caracteres de escape) y también permite hacer referencia a variables dentro de la cadena (como `atom`).
- **`({atom})`**: Al utilizar `({atom})`, estás creando un grupo de captura para cada `atom`. Esto significa que cualquier coincidencia de un número, expresión entre paréntesis o identificador que aparezca antes y después del operador `^` será capturada como un grupo.
- **`\s*\^\s*`**: Este patrón es para el operador de potencia (`^`) y permite espacios opcionales antes y después de este operador.

### Conclusión

En resumen, el uso de `atom` como un subpatrón mejora la claridad y la mantenibilidad del código.
Has extraído la parte repetitiva de la expresión regular y la has definido una vez, permitiendo que `pattern` use ese grupo simplificado y mantenga el código más limpio.
Esto también facilita cualquier futura modificación en el patrón `atom`, ya que solo tendrás que hacerlo en un lugar.
"""
