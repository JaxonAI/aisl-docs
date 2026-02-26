# Grammar Reference

This page provides the formal grammar of AISL in EBNF-like notation, derived from
the ANTLR4 grammar definition.

## Program structure

```
program         = { statement } EOF

statement       = declaration
                | expression ";"
                | assignment ";"
                | return_statement ";"
                | for_statement
                | append_statement ";"
```

## Declarations

```
declaration     = "declare" IDENTIFIER "as" decl_type

decl_type       = model_decl
                | dataset_decl
                | performance_decl
                | file_decl
                | function_decl
```

### Model declaration

```
model_decl      = "model" [ "{" model_option { "," model_option } "}" ]

model_option    = model_keyword "=" ( IDENTIFIER | STRING | NUMBER | record_literal )

model_keyword   = "endpoint" | "model_name" | "temperature" | "max_tokens"
                | "top_p" | "frequency_penalty" | "presence_penalty"
                | "timeout" | "response_format" | "response_schema"
```

### Dataset declaration

```
dataset_decl    = "dataset" "{" IDENTIFIER { "," option } "}"
```

### Performance declaration

```
performance_decl = "performance" "{" metric_decl { "," metric_decl } "}"

metric_decl     = "metric" "[" IDENTIFIER "]" "(" [ parameters ] ")" condition

condition       = [ sub_expression [ consequent ] ]

consequent      = "?" STRING ":" STRING
```

### File declaration

```
file_decl       = "file" "{" option { "," option } "}"

option          = keyword "=" IDENTIFIER

keyword         = "model" | "key" | "name" | "type"
```

### Function declaration

```
function_decl   = "function" "(" [ parameters ] ")" "{" block "}"

parameters      = IDENTIFIER { "," IDENTIFIER }

block           = statement { statement }
```

## Statements

```
assignment      = "let" IDENTIFIER "=" expression

for_statement   = "for" NUMBER ".." NUMBER "{" block "}"

append_statement = "append" IDENTIFIER "with" expression

return_statement = "return" expression
```

## Expressions

```
expression      = term sub_expression

sub_expression  = OPERATOR term sub_expression
                | (* empty *)

term            = IDENTIFIER
                | NUMBER
                | function_call
                | "(" expression ")"
                | STRING
                | list_literal
                | record_literal

list_literal    = "[" [ expression { "," expression } ] "]"

record_literal  = "{" STRING ":" expression { "," STRING ":" expression } "}"

function_call   = IDENTIFIER "(" arguments ")"

arguments       = expression { "," expression }
```

## Lexical rules

```
NUMBER          = digit { digit } [ "." digit { digit } ]

IDENTIFIER      = ( letter | "_" ) { letter | digit | "_" }

STRING          = '"' { string_char } '"'

string_char     = any character except '"', '\', CR, LF
                | '\' any_character

OPERATOR        = "+" | "-" | "*" | "/"
                | "==" | "!=" | "<=" | ">=" | "<" | ">"
                | "&&" | "||" | "!"

LINE_COMMENT    = "//" { any character except CR, LF }

BLOCK_COMMENT   = "/*" { any character } "*/"
```

Where `letter` is `[a-zA-Z]` and `digit` is `[0-9]`.

## Operator table

| Symbol | Type | Description |
|--------|------|-------------|
| `+` | Arithmetic | Addition |
| `-` | Arithmetic | Subtraction |
| `*` | Arithmetic | Multiplication |
| `/` | Arithmetic | Division |
| `==` | Comparison | Equal |
| `!=` | Comparison | Not equal |
| `<` | Comparison | Less than |
| `>` | Comparison | Greater than |
| `<=` | Comparison | Less than or equal |
| `>=` | Comparison | Greater than or equal |
| `&&` | Logical | AND |
| `\|\|` | Logical | OR |
| `!` | Logical | NOT |
| `?` `:` | Ternary | Conditional |
| `=` | Assignment | Assign (in `let` and declarations) |

## Punctuation

| Symbol | Usage |
|--------|-------|
| `{` `}` | Blocks, records, declarations |
| `[` `]` | Lists, metric invocations |
| `(` `)` | Grouping, function parameters |
| `,` | Separator |
| `;` | Statement terminator |
| `:` | Record key-value separator, ternary else |
| `?` | Ternary condition |
| `..` | Range operator (in `for` loops) |
