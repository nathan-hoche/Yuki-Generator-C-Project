void my_puts(char *str)
{
    for (int x = 0; str[x] ;x++)
        write(1, &str[x], 1);
    write(1, "\n", 1);
}