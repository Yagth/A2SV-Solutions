import Data.List (intersperse, sort, intercalate)
main :: IO ()
main = do
    inputs <- getLine
    putStrLn $ helpfulMath inputs

helpfulMath :: String -> String
helpfulMath = intersperse '+' . sort . filter (/= '+')