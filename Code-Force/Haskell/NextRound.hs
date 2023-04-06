import Data.List (group)
main :: IO()
main = do
    inputs <- getLine
    scoreStr <- getLine
    let [_, k] = words inputs
        scores = map read $ words scoreStr
        kth = scores !! (read k - 1)
        next = nextRound scores kth
    print next

nextRound :: [Int] -> Int-> Int
nextRound xs kth = length $ filter (\x -> x>=kth && x > 0) xs
