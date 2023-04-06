import Data.List(sort)

main :: IO ()
main = do
    input <- getContents
    let (_:pointStr:_:questionStr) = lines input
        points = map read (words pointStr)
        questions = map (map read . words) questionStr
        sortedPoints = sort points
        results = map (calcPoint points sortedPoints) questions
    mapM_ print results
 
calcPoint :: [Integer] -> [Integer] -> [Integer] -> Integer
calcPoint points sortedPoints [questionType, x, y]
    | questionType == 1 = sum' points (x,y)
    | questionType == 2 = sum' sortedPoints (x,y)
    | otherwise = 0
    where sum' :: [Integer] -> (Integer, Integer) -> Integer
          sum' points (x,y)
            | x > y = 0
            | otherwise = sum $ drop (x' - 1) $ take y' points
          x' = fromInteger x
          y' = fromInteger y