import ssl
import socket
import datetime

def get_ssl_expiry_date(hostname, port=443):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                not_after_str = cert['notAfter']
                expiry_date = datetime.datetime.strptime(not_after_str, '%b %d %H:%M:%S %Y %Z')
                return expiry_date
    except Exception as e:
        return None

if __name__ == "__main__":
    website = "example.com"  # Replace with the website you want to check
    expiry_date = get_ssl_expiry_date(website)

    if expiry_date:
        print(f"The SSL certificate for {website} expires on {expiry_date}.")
    else:
        print(f"Failed to retrieve SSL certificate information for {website}.")
