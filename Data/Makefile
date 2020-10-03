### Do not touch ####
SRC	=

FLAGS	=

MAKE_LIB = make -C ./lib/my/
#####################

NAME	=		a.out

OBJ		=		$(SRC:.c=.o)

all:	$(OBJ)
### Do not touch ####
		$(MAKE_LIB)
#####################
		gcc $(OBJ) -o $(NAME) $(FLAGS)

clean:
		rm -f $(OBJ)
		rm -f *~
		rm -f *\#
		rm -f *.o

fclean:	clean
		rm -f $(NAME)

re: 	fclean all

.PHONY: clean, fclean, re, all