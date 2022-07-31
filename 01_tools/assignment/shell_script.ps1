

mkdir shell_test
    
cd shell_test
touch test_print.py
cat > test_print.py << "END_SCRIPT"
END_SCRIPT
 
    
mv test_print.py new_test_print.py
    
ls shell_test
  
python new_test_print.py
    
rm -r shell_test

