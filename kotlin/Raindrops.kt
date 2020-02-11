object Raindrops {

    fun convert(n: Int): String {
        var soundString = ""
        if (n % 3 == 0){
            soundString += "Pling"
        }
        if (n % 5 == 0){
            soundString += "Plang"
        }
        if (n % 7 == 0){
            soundString += "Plong"
        }
        return if (soundString == ""){
            n.toString()
        }else{
            soundString
        }
    }
}
