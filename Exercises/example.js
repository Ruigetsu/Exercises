function is_prime(n) {
    for (let i = 2; i<n; i ++) {
        if (n % i == 0) return false
        else {
            return true
        }
    }
}
function all_primes(n){
    for (let j = 2; j < n; j++) {
        if (is_prime(j) == true) {
            console.log(j)
        }
    }
}
console.log(all_primes(10)) 