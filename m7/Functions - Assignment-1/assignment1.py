"""balance"""
def paying_debt_offinayear(balance, a_i_r, monthlypaymentrate):
    temp = balance
    months = 12
    while months >= 1:
        m_i_r = a_i_r / 12.0
        m_m_p = monthlypaymentrate * temp
        m_u_b = temp - m_m_p
        var = m_i_r*m_u_b
        u_b_e_m = m_u_b + (var)
        temp = u_b_e_m
        months = months - 1
    return(round(temp, 2))
def main():
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance:",paying_debt_offinayear(data[0],data[1],data[2]))
if __name__ == "__main__":
    main()
