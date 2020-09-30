int my_putstr(char *str)
{
    for (int x = 0; str[x] ;x++)
        write(1, &str[x], 1);
}