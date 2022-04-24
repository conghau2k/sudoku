#Hàm tìm những ô số còn trống giá trị, nếu tìm được các tham số row, col sẽ đặt vào vị trí chưa được gán và trả về true
#Nếu không còn mục nào trống thì trả về false
#L là một biến danh sách từ hàm solve_sudoku để theo dõi chỉ số của hàng cột
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False
#Hàm xét xem số num đã xuất hiện trên hàng chưa, nếu có trả về true, chưa trả về false
def used_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False
#Hàm xét xem số num đã xuất hiện trên cột chưa, nếu có trả về true, chưa trả về false
def used_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False
#Hàm xét xem số num đã xuất hiện trên lưới 3x3 chưa, nếu có trả về true, chưa trả về false
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False
#Kiểm tra xem có hợp lệ để gám num cho hàng, cột, lưới 3x3 tương ứng không 
def check_location_is_safe(arr, row, col, num):
    #Kiểm tra xem num có thích hợp để gán cho ô không
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3,col - col % 3, num)

def solve_sudoku(arr):
    #L là một biến danh sách giữ bản ghi chỉ số hàng cột trong hàm find_empty_location
    l =[0, 0]
    #Nếu không có vị trí trống, return True
    if(not find_empty_location(arr, l)):
        return True
    print(l)
    #Gán giá trị của danh sách cho hàng và cột nhận được từ hàm trên
    row = l[0]
    col = l[1]
    #Xét chỉ số từ 1-9 
    for num in range(1, 10):
        #Nếu num thỏa
        if(check_location_is_safe(arr, row, col, num)):
            #Thực hiện gán
            arr[row][col]= num
            print(num)
            if(solve_sudoku(arr)):
                return True
            arr[row][col] = 0       
    return False

def check_correct(lst):
    #Xét theo hàng
    for i in range(0,9):
        row_vector = [] #Tạo một mảng để xét các phần tử
        for j in range(0,9):
            if lst[i][j] != 0:
                row_vector.append(lst[i][j]) #Thêm phần tử đang xét vào mảng xét
                if row_vector.count(lst[i][j]) > 1: #Nếu phần tử xuất hiện quá 1 lần kết quả sai, trả về 0
                    return 0
    #Xét theo cột
    for j in range(0,9):
        column_vector = []
        for i in range(0,9):
            if lst[i][j] != 0:
                column_vector.append(lst[i][j])
                if column_vector.count(lst[i][j]) > 1:
                    return 0

    for i in range(0,9):
        if i % 3 == 0:
            chunk_vector = []
        for j in range(0,3):
            if lst[i][j] != 0:
                chunk_vector.append(lst[i][j])
                if chunk_vector.count(lst[i][j]) > 1:
                    return 0
    for i in range(0,9):
        if i % 3 == 0:
            chunk_vector = []
        for j in range(3,6):
            if lst[i][j] != 0:
                chunk_vector.append(lst[i][j])
                if chunk_vector.count(lst[i][j]) > 1:
                    return 0
    for i in range(0,9):
        if i % 3 == 0:
            chunk_vector = []
        for j in range(6,9):
            if lst[i][j] != 0:
                chunk_vector.append(lst[i][j])
                if chunk_vector.count(lst[i][j]) > 1:
                    return 0

