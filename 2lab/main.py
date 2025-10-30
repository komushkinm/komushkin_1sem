

if __name__ == "__main__":
    pass # Ваш код здесь

def converter():
    
    exchange_rate = input().replace(',', '').split() 
    exchange_path = input().replace(',', '').split() 

    ## неправильный ввод (кол-во символов не подходит под шаблон)
    if len(exchange_rate) % 3 != 0:
        print("Ошибка: Неправильное количество элементов в курсах валют")
        return

    rates_list = []

    for i in range(0, len(exchange_rate), 3):
        
                from_currency = exchange_rate[i]
                to_currency = exchange_rate[i + 1]
                kurs_valut = float(exchange_rate[i + 2])

                rates_list.append((from_currency, to_currency, kurs_valut))

    
    ## обработка неправильного ввода в пути конвертации
    if len(exchange_path) < 3:
        print("Ошибка: Слишком мало элементов в запросе")
        return
                
    start_price = float(exchange_path[0])
    path = exchange_path[1:]

    current_amount = start_price
    current_currency = path[0]
    result_steps = [f"{current_amount} {current_currency}"]


    for i in range(len(path) - 1):
        from_curr = path[i]
        to_curr = path[i + 1]
        
        found_rate = None
        for rate_from, rate_to, rate_val in rates_list:
            if rate_from == from_curr and rate_to == to_curr:
                found_rate = rate_val
                break
        
        if found_rate is None:
            print(f"ОШИБКА: Не найден курс из '{from_curr}' в '{to_curr}'")
            return
        
        new_amount = current_amount * found_rate
        print(f"Шаг {i+1}: {current_amount} {from_curr} * {found_rate} = {new_amount} {to_curr}")
            
        current_amount = new_amount
        current_currency = to_curr
        
        result_steps.append(f"{current_amount:.2f} {current_currency}")
        

    print(" -> ".join(result_steps))

converter()
