%{
	#include <stdio.h>

	void yyerror(char *error){
		printf("Error: %s", error);
	}
%}

%token IDENTIFIER CONSTANT STRING_LITERAL
%token EQ_OP
%token CHAR INT CONST
%token IF WHILE RETURN

%start translation_unit
%%

primary_expression
	: IDENTIFIER
	| CONSTANT
	| STRING_LITERAL
	| '(' assignment_expression ')'
	;

postfix_expression
	: primary_expression
	| postfix_expression '[' assignment_expression ']'
	| postfix_expression '(' ')'
	| postfix_expression '(' argument_expression_list ')'
	;

argument_expression_list
	: assignment_expression
	| argument_expression_list ',' assignment_expression
	;

unary_expression
	: postfix_expression
	| unary_operator unary_operator
	;

unary_operator
	: '&'
	| '*'
	;

multiplicative_expression
	: unary_expression
	| multiplicative_expression '*' unary_expression
	| multiplicative_expression '/' unary_expression
	;

additive_expression
	: multiplicative_expression
	| additive_expression '+' multiplicative_expression		{printf("Suma");}
	| additive_expression '-' multiplicative_expression		{printf("Resta");}
	;

relational_expression
	: additive_expression
	| relational_expression '<' additive_expression
	| relational_expression '>' additive_expression
	;

equality_expression
	: relational_expression
	| equality_expression EQ_OP relational_expression
	;

assignment_expression		
	: equality_expression
	| unary_expression '=' assignment_expression
	 {
		// prototipo de regla semántica:
		printf("1. Calcular/obtener el valor de la expresión");
		printf("2. Obtener la dirección de VARIABLE.");
		printf("3. Copiar el valor de la expresioń a la dirección de\
		VARIABLE" );
    }
	;

declaration
	: declaration_specifiers init_declarator_list ';'
	;

declaration_specifiers
	: type_specifier
	| CONST
	| CONST declaration_specifiers
	;

init_declarator_list
	: init_declarator
	| init_declarator_list ',' init_declarator
	;

init_declarator
	: direct_declarator
	| direct_declarator '=' assignment_expression
	;

type_specifier
	: CHAR
	| INT
	;

direct_declarator
	: IDENTIFIER
	| '(' direct_declarator ')'
	| direct_declarator '[' ']'
	| direct_declarator '(' parameter_list')'
	| direct_declarator '(' identifier_list ')'
	| direct_declarator '(' ')'
	;

parameter_list
	: parameter_declaration
	| parameter_list ',' parameter_declaration
	;

parameter_declaration
	: declaration_specifiers direct_declarator
	| declaration_specifiers
	;

identifier_list
	: IDENTIFIER
	| identifier_list ',' IDENTIFIER
	;

statement
	: IDENTIFIER ':' statement
	| compound_statement
	| expression_statement
	| IF '(' assignment_expression ')' statement 
	| WHILE '(' assignment_expression ')' statement
	| RETURN assignment_expression ';'
	;

compound_statement
	: '{' statement_list '}'
	| '{' declaration_list '}'
	| '{' declaration_list statement_list '}'
	;

declaration_list
	: declaration
	| declaration_list declaration
	;

statement_list
	: statement
	| statement_list statement
	;

expression_statement
	: ';'
	| assignment_expression ';'
	;

translation_unit
	: external_declaration
	| translation_unit external_declaration
	;

external_declaration
	: function_definition			{printf("function_definition");}
	| declaration					{printf("declaration");}
	;

function_definition
	: declaration_specifiers direct_declarator compound_statement
	;

%%

int main(void){	
	yyparse();
}