D			[0-9]
L			[a-zA-Z_]
FS			(f|F|l|L)
IS			(u|U|l|L)*

%{
#include <stdio.h>
#include "parser.tab.h"

check_type();
%}

%%
"/*"							{ comment(); }
"char"							{ return(CHAR); }
"const"							{ return(CONST); }
"if"							{ return(IF); }
"int"							{ return(INT); }
"return"						{ return(RETURN); }
"while"							{ return(WHILE); }

{L}({L}|{D})*					{ return(check_type()); }
{D}+{IS}?						{ return(CONSTANT); }

L?'(\\.|[^\\'])+'				{ return(CONSTANT); }
L?\"(\\.|[^\\"])*\"				{ return(STRING_LITERAL); }
"=="							{ return(EQ_OP); }
";"								{ return(';'); }
("{"|"<%")						{ return('{'); }
("}"|"%>")						{ return('}'); }
","								{ return(','); }
"="								{ return('='); }
"("								{ return('('); }
")"								{ return(')'); }
("["|"<:")						{ return('['); }
("]"|":>")						{ return(']'); }
"-"								{ return('-'); }
"+"								{ return('+'); }
"*"								{ return('*'); }
"/"								{ return('/'); }
"<"								{ return('<'); }
">"								{ return('>'); }
"&"								{ return('&'); }
"%"								{ return('%'); }
.								{ /* ignore bad characters */ }

%%

yywrap()
{
	return(1);
}


comment()
{
	char c, c1;

loop:
	while ((c = input()) != '*' && c != 0)
		putchar(c);

	if ((c1 = input()) != '/' && c != 0)
	{
		unput(c1);
		goto loop;
	}

	if (c != 0)
		putchar(c1);
}

int check_type()
{
/*
* pseudo code --- this is what it should check
*
*	if (yytext == type_name)
*		return(TYPE_NAME);
*
*	return(IDENTIFIER);
*/

/*
*	it actually will only return IDENTIFIER
*/

	return(IDENTIFIER);
}
