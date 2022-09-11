
fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
    val bw = System.`out`.bufferedWriter()

    bw.use { w ->
        w.write("${palisNotPal(readLine())}")
    }
}

fun palisNotPal (target: String) : Int {
    val n = target.length
    var isPal = false

    for(i in 0 until n/2) {
        // 하나라도 다르면 회문 아님
        // ex. PALINDROME
        if(target[i] != target[n-1-i]) {
            return n
        }

        // 모두 같은 글자인지 체크
        else if(target[i] != target[i+1]) {
            isPal = true
        }
    }

    // 회문일 때 ex. ABCBA or ZZZ
    return if(isPal) n-1 else -1
}
