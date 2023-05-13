import Data.List(group, sort)

main :: IO ()
main = interact $ displayString . numberOfTimes . (\xs -> let [_, second] = lines xs in second)

numberOfTimes :: String -> [String]
numberOfTimes = group . sort

displayString :: [String] -> String
displayString [a] = if head a == 'A' then "Anton" else "Danik"
displayString [a,b] | length a > length b = "Anton" | length b > length a = "Danik" | otherwise = "Friendship"