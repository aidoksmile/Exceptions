# 1. Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), 
# и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению 
# приложения, вместо этого, необходимо повторно запросить у пользователя ввод данных.

def get_float_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Ошибка: введено некорректное значение, введите число.")

num = get_float_input("Введите дробное число: ")
print(f"Введенное число: {num}")

# 2. Если необходимо, исправьте данный код 
# (задание 2 https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)

try {
   int d = 2;
   double catchedRes1 = intArray[8] / d;
   System.out.println("catchedRes1 = " + catchedRes1);
} catch (ArithmeticException e) {
   System.out.println("Catching exception: " + e);
}

# 3. Дан следующий код, исправьте его там, где требуется 
# (задание 3 https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit)

public static void main(String[] args) throws Exception {
   try {
       int a = 90;
       int b = 3;
       System.out.println(a / b);
       printSum(23, 234);
       int[] abc = { 1, 2 };
       abc[3] = 9;
   } catch (NullPointerException ex) {
       System.out.println("Указатель не может указывать на null!");
   } catch (IndexOutOfBoundsException ex) {
       System.out.println("Массив выходит за пределы своего размера!");
   } catch (Exception ex) {
       System.out.println("Что-то пошло не так...");
   }
}


# 4. Разработайте программу, которая выбросит Exception, 
# когда пользователь вводит пустую строку. Пользователю должно показаться сообщение, 
# что пустые строки вводить нельзя.

def get_input():
    user_input = input("Введите строку: ")
    if not user_input:
        raise Exception("Вы ввели пустую строку!")
    return user_input

try:
    print(get_input())
except Exception as e:
    print(e)
