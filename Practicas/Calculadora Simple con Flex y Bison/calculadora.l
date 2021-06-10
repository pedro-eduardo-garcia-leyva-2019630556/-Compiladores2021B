
%{
    #include "calculadora.tab.h"
    #include<string.h>
    #include<stdio.h>
%}

%%
        /*Reglas*/
[0-9]+      { sscanf(yytext, "%lf", &yylval);
              return NUMERO;
            }
[*]         {return '*';}
[+]         {return '+';}
\n          {return '\n';}
[ ]
.
%%



