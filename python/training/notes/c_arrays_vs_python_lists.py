
'''
C:
-------------------------------------------------------    

structs -- fixed size, fields are accessible by name:           employee.age employee.ssn
           non-homogenous                                       unsigned short, char [9]           
           
arrays  -- fixed size, fields are indexable by number:          employee[50] employee[80]
           homogeneous with respect to type

           struct Employee * personnel[50];
           double temperature_readings[75];

Python:
-------------------------------------------------------
tuples -- fixed length, immutable, typically non-homogenous     ee = ('Raymond', 'Hettinger', 0x36, 'raymond.hettinger')
                                                                       str           str       int      str
          fields accesses by number                             ee[0]
                                                                ee[2]
named tuple -- adds field names                                 ee.first_name      ee.age                                                                

lists  -- dynamic, variant arrays                               s = ['ten', 'twenty', 30]
                     ^-- allowed to be non-homogenous                 str     str     int
             ^---------- size changing                          s.append(40) 

          implemented with C arrays of pointers                 Python containers don't actually contain things
          dense data structures                                 They have references to their contents
          


----

struct StrObject {
    ssize_t refcnt = 1;
    PyType * __class__ = str;
    ssize_t len = 5;
    char data[5] = {"h", "e", "l", "l", "o"};
}

char *s = {"hello"};
printf("%s", strlen(s));     // 5

-----

struct ListObject {
    ssize_t refcnt;                 # sys.getrefcount(s)
    PyType __class__;               # s.__class__ or type(s)
    ssize_t size;                   # s.__len__() or len(s)
    ssize_t alloc_size;
    PyObject *data;
}


s = [10, 20, 30]

o = malloc(sizeof(ListObject))
o->refcnt = 1;
o->__class__ = &PyListType
o->size = 0
o->alloc_size = 0
o->data = NULL

p = malloc(sizeof(IntObject)
p->refcnt = 1;
p->__class__ = &PyIntType
p->value = 10;

o->alloc_size = 4
o->data = malloc(sizeof(PyObject *) * 4)

o->size = 1
o->data[0] = p

p = malloc(sizeof(IntObject)
p->refcnt = 1;
p->__class__ = &PyIntType
p->value = 20;

o->size = 2
o->data[1] = p

# s = [10, 20, 30, 40, 50]
o->alloc_size = 8
o->data = realloc(o->data, sizeof(PyObject *) * 8)

'''
