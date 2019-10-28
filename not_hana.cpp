//
// Created by 23212 on 2019/10/29.
//


#include <stdint-gcc.h>
#include <c++/4.8.3/iostream>

template <typename T, typename... Y>
struct Schema{
    explicit Schema(uint16_t typeOfTlv, Y... y) : type{typeOfTlv} {};
    using gen = T;

    //auto find(Y... y){};
    uint16_t type;
};

//template <typename T>
//struct Schema<typename T>

struct x1{};
struct y1{};
struct y2{};
struct z1{};
struct z2{};
struct z3{};
struct z4{};

Schema<z1> c1{3};
Schema<z2> c2{4};
Schema<z3> c3{5};
Schema<z4> c4{6};
Schema<y1, z1, z2> s1{1, z1{}, z2{}};
Schema<y2, z3, z4> s2{2, z3{}, z4{}};
Schema<x1, decltype(s1), decltype(s2)> s{0, s1, s2};

template <typename T, typename... A>
void go(uint16_t typeOfTlv, T t, A... a)
{
    if (typeOfTlv == t.type){
        //流入T::gen类型的变量
        std::cout << typeOfTlv << std::endl;
    } else {
        go(typeOfTlv, a...);
    }
}

template <typename T>
void go(uint16_t typeOfTlv, T t)
{
    //前面都不是，那就一定是最后一个，流入T::gen类型的变量
    std::cout << t.type << std::endl;
}



int main(){
    uint16_t subTlvType = 1;
    go(subTlvType, s);
}