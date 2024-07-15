
CONSTANT_BONUS = 1000

# 1.O programa deve começar solicitando ao usuário que insira seu nome.
user_name = input("Insert your name: ")

# 2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
user_salary = float( input("Insert your salary: "))

# 3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
user_bonus_perc = float( input("Insert your bonus: "))
# 4. O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
bonus_value = CONSTANT_BONUS + user_salary * user_bonus_perc

# 5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f"Hello {user_name}, your bonus was {bonus_value}.")