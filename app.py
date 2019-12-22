from datetime import datetime
from flask import Flask, render_template
import json
import requests
from job_dict import job_dict

app = Flask(__name__)

#testmode = os.getenv("TESTMODE", False)


def connectSheets():
    url = 'https://spreadsheets.google.com/feeds/list/1zBeYVkoyLavJIIBKJ9aG8ID_ZtLe-UHeKK72hk_ZKfE/1/public/values?alt=json'
    jobs = json.loads(requests.get(url).text)['feed']['entry']
    job_dict = []
    for each in jobs:
        timestamp = datetime.strptime(each['gsx$timestamp']['$t'].strip(), '%m/%d/%Y')
        postedby = each['gsx$postedby']['$t']
        company = each['gsx$company']['$t']
        role = each['gsx$role']['$t']
        location = each['gsx$location']['$t']
        remote = each['gsx$remote']['$t']
        remoterestrictions = each['gsx$remoterestrictions']['$t']
        salaryrange = each['gsx$salaryrange']['$t']
        visasponsorship = each['gsx$visasponsorship']['$t']
        url = each['gsx$url']['$t']
        contact = each['gsx$contact']['$t']
        descriptionornotes = each['gsx$descriptionornotes']['$t']
        
        job_dict.append({"timestamp": timestamp, 
                "postedby" : postedby,
                "location" : location,
                "company": company,
                "role": role,
                "remote" : remote,
                "remoterestrictions" : remoterestrictions,
                "salaryrange" : salaryrange,
                "visasponsorship" : visasponsorship,
                "url" : url,
                "contact" : contact,
                "descriptionornotes" : descriptionornotes
        })


        print('job dict:')
        #print(job_dict)
        print('\n\n\n')
        #job_dict.reverse()
    #sorted(job_dict, key=lambda item: (item['timestamp']))
    job_dict = sorted(job_dict, key=lambda item: item['timestamp'])
    return job_dict

@app.route('/')
def main():
    jobs = connectSheets()
    #print(jobs)
    #jobs = job_dict
    #jobs.reverse()

    #sorted(each.items(), reverse=True)
    return render_template('base.html', jobs=jobs)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8001')

