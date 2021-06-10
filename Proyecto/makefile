compile: parser.y lexer.l
	bison -d parser.y
	flex lexer.l
	gcc -c parser.tab.c
	gcc -c lex.yy.c
	gcc lex.yy.o parser.tab.o -lfl -o proyecto