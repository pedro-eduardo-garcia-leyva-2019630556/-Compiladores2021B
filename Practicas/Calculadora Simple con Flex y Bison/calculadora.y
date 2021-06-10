%{
    // Reverse Polish Notation calculator.

    #include<stdio.h>
    #include<math.h>

    void yyerror (char *message){
        printf("Error: %s", message);
    }

%}
    /* Definiciones de tokens */

%define api.value.type {double}
%token NUMERO
%left '-' '+'
%left '*' '/'
%precedence NEG
%right '^'

%% /*Grammar rules and actions follow */

entrada:
%empty
| entrada linea
;

linea:
  '\n'
| expresion '\n'            { printf("\t%.10g\n", $1); } 
;

expresion:
  NUMERO                      { $$ = $1; }
| expresion '+' expresion    { $$ = $1 + $2; }
| expresion '*' expresion    { $$ = $1 * $2; }
| expresion '/' expresion     { $$ = $1 / $3; }
| '-' expresion %prec NEG     { $$ = -$2; }
| expresion '^' expresion     { $$ = pow($1, $3); }
| '(' expresion ')'           { $$ = $2; }
;
%%
 
int main(void) {
    return yyparse();
}


// int yylex(void) {

//     int c;

//     // Se salta los espacios en blanco
//     while ((c = getchar()) == ' ' || c == '\t')
//         continue;

//     // Procesa los numeros
//     if (c == '.' || isdigit(c)){
//         ungetc(c, stdin);
//         scanf("%lf", &yylval);
//         return NUMERO;
//     }

//     // Regresa el fin de entrada
//     if (c == EOF)
//         return 0;
    
//     // Retorna un solo caracter
//     return c;
// }