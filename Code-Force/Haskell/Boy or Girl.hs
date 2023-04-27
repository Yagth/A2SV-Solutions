import Data.List(nub)

main :: IO ()
main = (putStrLn . boyVsGirl) =<< getLine

boyVsGirl :: String -> String
boyVsGirl xs | odd $ length $ nub xs = "IGNORE HIM!" | otherwise = "CHAT WITH HER!"