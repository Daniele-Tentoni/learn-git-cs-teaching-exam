#!/usr/bin/env expect

# Questo script potrebbe essere utilizzato per controllare che l'esercizio svolto dallo studente sia corretto o meno. Per eseguirlo su un runner di Github deve prima essere installato expect (nemmeno sulla mia macchina Ubuntu era preinstallato).

# Ovviamente si puo' testare l'output del programma anche con pipe e redirezionamenti, ma ho trovato questa modalita' piu' ordinata.

spawn ./phonebook.py

expect {
    -exact "PyPhonebook: digit a command and enter (help for more info): " { send "ls\r" }
    timeout { puts "Timeout"; exit 1 }
}

expect {
    -exact "No contacts" { puts "ok" }
    timeout { puts "Why contacts"; exit 1 }
}

send "new\r"

expect {
    "Input contact nickname: " { send "t" { expect -re {
        "Input contact name: " { send "d" { expect -re {
            "Input contact surname: " { send "t" { expect -re {
                "Input contact email: " { send "e" {
                    exit 0
                }}
                ".*" { puts "fail"; exit 1 }
            }}}
            ".*" { puts "fail"; exit 1 }
        }}}
        ".*" { puts "fail"; exit 1 }
    }}}
    ".*" { puts "fail"; exit 1 }
}

puts "Unreachable code"
exit 2
