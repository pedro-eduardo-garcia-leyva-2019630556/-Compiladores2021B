
%{
    #include<stdio.h>
    #include "mfcalc.tab.h"
    // #include "tablaS.h"
%}
%option header-file="lex.yy.h"
%%
        /*Reglas*/
[0-9]+      { sscanf(yytext, "%lf", &yylval.NUM);
              return NUM;
            }
[*]         {return '*';}
[+]         {return '+';}
\n          {return '\n';}
[ ]
.
%%


