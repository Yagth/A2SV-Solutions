main :: IO ()
main = interact $ show . sub . map read . words

sub :: [Int] -> Int
sub [n, count] 
    | count == 0 = n
    | n `mod` 10 == 0 = sub [n `div` 10 , count - 1] 
    | otherwise = sub [n - 1, count - 1]