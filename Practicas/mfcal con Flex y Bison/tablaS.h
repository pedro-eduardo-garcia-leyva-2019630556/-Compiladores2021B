/* Tabla de simbolos: mantiene un seguimiento de los nombres y significado
    de las variables y funciones */

// #include "mfcalc.tab.h"
// #include<math.h>
#include "mfcalc.tab.h"
#include<stdlib.h>
#include<string.h>

typedef double (*func_t) (double);

struct symrec {
    char *name;
    int type;
    union
    {
        double var;
        func_t fnctptr;
    } value;
    struct symrec *next;
};

typedef struct symrec symrec;

extern symrec *sym_table;

symrec *putsym (char const *, int);
symrec *getsym (char const *);

struct init{
    char const *fname;
    double (*fnct) (double);
    // func_t *fnctptr;
};

struct init const arith_fncts[] = {
    { "atan", atan },
    { "cos", cos   },
    { "exp", exp   },
    { "ln", log    },
    { "sin", sin   },
    { "sqrt", sqrt },
    { 0, 0 },
};

symrec *sym_table;

// Pone las funciones en la tabla

// static void init_table(void){
//     int i;
//     for(i=0; arith_fncts[i].fname; i++){
//         symrec *ptr = putsym(arith_fncts[i].fname, );
//         ptr -> value.fnctptr = arith_fncts[i].fnctptr;
//     }
// }

symrec* putsym (char const *sym_name, int sym_type){
    symrec *ptr = (symrec *) malloc(sizeof(symrec));
    ptr -> name = (char*) malloc(strlen(sym_name) + 1);
    strcpy(ptr->name, sym_name);
    ptr -> type = sym_type;
    ptr -> value.var = 0;
    ptr -> next = (struct symrec *) sym_table;
    sym_table = ptr;
    return ptr;
}

symrec * getsym (char const *sym_name) {
    symrec *ptr;
    for (ptr = sym_table; ptr != (symrec *) 0; ptr = (symrec * ) ptr -> next)
        if(strcmp(ptr->name, sym_name) == 0)
            return ptr;
        return 0;
}

 