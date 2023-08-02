if [-d "env"]
then 
    echo "Python virtual env exist"
else
    python -m venv env
fi

echo $PWD
source env\Scripts\activate

pip install -r requirements.txt

if [-d "logs"]
then 
    echo "log folder exist"
else
    mkdir logs
    touch logs/errors.log logs/access.log
fi
sudo chmod -R 777 logs
echo "envsetup finishes"