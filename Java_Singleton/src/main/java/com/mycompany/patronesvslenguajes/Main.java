/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.patronesvslenguajes;

/**
 *
 * @author steve
 */
public class Main {

    public static void main(String[] args) {
        System.out.println("Si ves el mismo valor, entonces se reutilizó el Singleton (¡Bien!)." + "\n" +
                "Si ves diferentes valores, entonces se crearon dos Singletons (¡Mal!)." + "\n\n" +
                "RESULTADO:" + "\n");

        Singleton singleton1 = Singleton.getInstance("FOO");
        
        Singleton singleton2 = Singleton.getInstance("BAR");

        System.out.println(singleton1.value);
        System.out.println(singleton2.value);
    }
}
