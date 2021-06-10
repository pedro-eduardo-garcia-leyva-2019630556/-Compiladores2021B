%{
    // Multi-fuction Calc

    #include<stdio.h>
    #include<math.h>
    #include "tablaS.h" /* Contiene definiciones de symrec*/

    void yyerror (char *message){
        printf("Error: %s", message);
    }

%}
    /* Definiciones de tokens */

%define api.value.type union
%token <double> NUM
%token <symrec*> VAR FNCT /* apuntador a la tabla de simbolos: variable y funcion*/
%type <double> exp

%precedence '='
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
| exp '\n'            { printf("\t%.10g\n", $1); } 
;

exp:
  NUM                     { $$ = $1; }
| VAR                   { $$ = $1->value.var; }
| VAR '=' exp           { $$ = $3; $1->value.var = $3; }
| FNCT '(' exp ')'   { $$ = (*($1->value.fnctptr))($3);}
| exp '+' exp         { $$ = $1 + $3; }
| exp '*' exp         { $$ = $1 * $3; }
| exp '/' exp         { $$ = $1 / $3; }
| '-' exp %prec NEG     { $$ = -$2; }
| exp '^' exp    { $$ = pow($1, $3); }
| '(' exp ')'           { $$ = $2; }
;
%%
 
int main(void) {
  for(int i=0; arith_fncts[i].fname; i++){
    symrec *ptr = putsym(arith_fncts[i].fname, FNCT);
    ptr -> value.fnctptr = arith_fncts[i].fnct;
  }
  return yyparse();
}

