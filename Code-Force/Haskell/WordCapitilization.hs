import Data.Char(toUpper)

main :: IO ()
main = (putStrLn <$> capitalize) =<< getLine
    where capitalize (x:xs) = toUpper x : xs