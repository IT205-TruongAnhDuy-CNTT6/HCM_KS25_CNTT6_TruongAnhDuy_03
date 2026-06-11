def validate_input(promt: str, input_type: str = "str"):
    while True:
        user_input = input(promt)
        if not user_input:
            print("Dữ liệu không được để trống!")
            continue
        if input_type == "int":
            user_input = int(user_input)
            try:
                if user_input < 0:
                    print("Dữ liệu không được âm!")
                    continue
            except:
                print("Dữ liệu không hợp lệ!")
                continue
        return user_input
    
def ranking(spending_total):
    if spending_total < 5000000:
        return {"discount_rate": "0%", "rank": "Đồng"}
    elif 5000000 <= spending_total < 15000000:
        return {"discount_rate": "2%", "rank": "Bạc"}
    elif 15000000 <= spending_total < 30000000:
        return {"discount_rate": "5%", "rank": "Vàng"}
    else:
        return {"discount_rate": "10%", "rank": "Kim cương"}
    
def menu():
    print("""
===== MENU =====
1. Hiển thị danh sách khách hàng
2. Đăng ký khách hàng mới
3. Cập nhật thông tin giao dịch
4. Xóa dữ liệu khách hàng
5. Tìm kiếm khách hàng
6. Thống kê phân hạng thành viên
7. Thoát chương trình""")
    
def show_list(customer_list):
    if not customer_list:
        print("Danh sách rỗng!")
        return
    print("===== DANH SÁCH KHÁCH HÀNG =====")
    print(f"{"Mã KH":<10} | {"Họ tên":<20} | {"Số điện thoại":<20} | {"Tổng chi tiêu":<20} | {"Số lần mua":<20} | {"Tỷ lệ chiết khấu":<20} | {"Hạng thành viên":<20}")
    for customer in customer_list:
        print(f"{customer.get("id"):<10} | {customer.get("name"):<20} | {customer.get("phone"):<20} | {customer.get("spending_total"):<20} | {customer.get("buying_count"):<20} | {ranking(customer.get("spending_total")).get("discount_rate"):<20} | {ranking(customer.get("spending_total")).get("rank"):<20}")

def add_customer(customer_list):
    id = validate_input("Nhập mã KH: ")
    name = validate_input("Nhập họ tên: ")
    phone = validate_input("Nhập số điện thoại: ")
    spending_total = validate_input("Nhập tổng chi tiêu: ", "int")
    buying_count = validate_input("Nhập số lần mua: ", "int")
    customer_list.append({"id": id, "name": name, "phone": phone, "spending_total": spending_total, "buying_count": buying_count})
    print("Đăng ký thành công!")
    print(f"Tỷ lệ chiết khấu: {ranking(spending_total).get("discount_rate")}")
    print(f"Hạng thành viên: {ranking(spending_total).get("rank")}")

def update_customer(customer_list):
    if not customer_list:
        print("Danh sách rỗng!")
        return
    id = validate_input("Nhập mã KH cần cập nhật: ")
    for customer in customer_list:
        if id.lower() == customer.get("id").lower():
            customer["phone"] = validate_input("Nhập số điện thoại mới: ")
            customer["spending_total"] = validate_input("Nhập tổng chi tiêu mới: ")
            customer["buying_count"] = validate_input("Nhập số lần mua mới: ")
            print("Cập nhật thành công!")
            print(f"Tỷ lệ chiết khấu mới: {ranking(customer.get("spending_total")).get("discount_rate")}")
            print(f"Hạng thành viên mới: {ranking(customer.get("spending_total")).get("rank")}")
            break
    else:
        print("Không tìm thấy mã KH!")

def delete_customer(customer_list):
    if not customer_list:
        print("Danh sách rỗng!")
        return
    id = validate_input("Nhập mã KH cần xóa: ")
    for customer in customer_list:
        if id.lower() == customer.get("id").lower():
            check = validate_input("Bạn có chắc muốn xóa khách hàng này khỏi hệ thống không? (Y/N): ")
            if check == "Y":
                del customer
                break
            elif check == "N":
                print("Chưa xóa khách hàng!")
                break
    else:
        print("Không tìm thấy mã KH!")

def search_customer(customer_list):
    if not customer_list:
        print("Danh sách rỗng!")
        return
    print("""
===== TIÊU CHÍ TÌM KIẾM =====
1. Tìm theo mã KH
2. Tìm gần đúng theo Tên khách hàng""")
    while True:
        choice = validate_input("Nhập lựa chọn: ")
        match choice:
            case 1:
                id = validate_input("Nhập mã KH cần tìm: ")
                for customer in customer_list:
                    if id.lower() == customer.get("id").lower():
                        print("===== DANH SÁCH KHÁCH HÀNG CẦN TÌM =====")
                        print(f"{"Mã KH":<10} | {"Họ tên":<20} | {"Số điện thoại":<20} | {"Tổng chi tiêu":<20} | {"Số lần mua":<20} | {"Tỷ lệ chiết khấu":<20} | {"Hạng thành viên":<20}")
                        print(f"{customer.get("id"):<10} | {customer.get("name"):<20} | {customer.get("phone"):<20} | {customer.get("spending_total"):<20} | {customer.get("buying_count"):<20} | {ranking(customer.get("spending_total")).get("discount_rate"):<20} | {ranking(customer.get("spending_total")).get("rank"):<20}")
                        break
                else: 
                    print("Không tìm thấy mã KH!")
                break

            case 2:
                print()

            case _:
                print("Lựa chọn không hợp lệ!")
    
def count_rank(customer_list):
    copper_rank = 0
    silver_rank = 0
    gold_rank = 0
    diamond_rank = 0
    for customer in customer_list:
        if customer.get("spending_total") < 5000000:
            copper_rank += 1
        elif 5000000 <= customer.get("spending_total") < 15000000:
            silver_rank += 1
        elif 15000000 <= customer.get("spending_total") < 30000000:
            gold_rank += 1
        else:
            diamond_rank += 1
    print(f"Số lượng KH hạng Đồng: {copper_rank}")
    print(f"Số lượng KH hạng Bạc: {silver_rank}")
    print(f"Số lượng KH hạng Vàng: {gold_rank}")
    print(f"Số lượng KH hạng Kim cương: {diamond_rank}")

def main():
    customer_list = [
        {"id": "KH001", "name": "Tran Minh Cuong", "phone": "0987654321", "spending_total": 12500000, "buying_count": 5}
    ]
    while True:
        menu()
        choice = validate_input("Nhập lựa chọn: ")
        match choice:
            case "1":
                show_list(customer_list)

            case "2":
                add_customer(customer_list)

            case "3":
                update_customer(customer_list)

            case "4":
                delete_customer(customer_list)

            case "5":
                search_customer(customer_list)

            case "6":
                count_rank(customer_list)

            case "7":
                print("Thoát chương trình!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")

main()