last_num = 0
i = 1
i_sum = 0
in_sequence = False
num = int(input("Digite um número: "))

while(i < num):
    i_sum = last_num + i
    if(i_sum == num): in_sequence = True
    last_num = i
    i = i_sum

if(in_sequence):
    print("Número está na sequência.")
else:
    print("Número não está na sequência.")
    
