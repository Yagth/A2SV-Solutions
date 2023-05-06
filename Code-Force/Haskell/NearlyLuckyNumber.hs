main :: IO ()
main = interact (nearlyLucky . luckyDigits)

luckyDigits :: String -> String
luckyDigits = filter (\x -> x == '4' || x == '7')

nearlyLucky :: String -> String
nearlyLucky xs | n == 4 || n == 7 = "YES" | otherwise = "NO"
    where n = length xs