DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

host="0.0.0.0"
port="8081"

while [ "$1" != "" ]; do
    case $1 in
        -h | --host)    host="$2"
                        shift;;
        -p | --port)    port="$2"
                        shift;;
    esac
    shift
done

gunicorn app:get_app --bind "${host}:${port}" --worker-class aiohttp.GunicornWebWorker