%{
	#include<math.h>
	#include<stdio.h>
%}

DIGIT	[0-9]
ID		[a-z][a-z0-9]*

%%

{DIGIT}+	{printf("An integer: %s (%d)\n", yytext, atoi(yytext));}

{DIGIT}+\.{DIGIT}*		{printf("A float: %s (%g)\n", yytext, atof(yytext));}

if|then|begin|end|function		{printf( "A keyword: %s\n", yytext);}

{ID}			{printf("An identifier: %s\n", yytext);}

.				printf("Unrecognized character: %s\n", yytext);

"{"[^{}\n]*"}"		// eat up 

%%

int main(int argc, char **argv){
	++argv, --argc;		// skipp over program name
	if(argc > 0)
		yyin = fopen(argv[0], "r");
	else
		yyin = stdin;
	yylex();
}
