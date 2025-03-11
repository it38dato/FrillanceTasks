#include <stdio.h>
    #define __USE_XOPEN
    #include <unistd.h>
    int main(int argc, char** argv)
    {
     if(argc==3)
       {
           printf("%s\n", crypt(argv[1],argv[2]));
       }
       else
       {
           printf("Использование: MyCrypt $пароль $salt\n" );
       }
      return 0;
    }