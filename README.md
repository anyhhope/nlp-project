# nlp-project


<img src="images/loss_plot.png" alt="loss plot" width="700">

Веса модели - https://drive.google.com/file/d/1whsdpFXYe55yREY33O5aCf7yCD5oHP7x/view?usp=sharing
---

### Utils

В папке utils скрипты, чтобы спарсить из логов tran loss и val loss и отобразить на графике. Логи можно выгрузить, если запускать обучаться ноутбук в кагле. Логи - принты ячеек

* Чтобы спарсить loss'ы в json

```bash
cd utils
python parse.py inheritune.log parsed_logs.json
```

* Чтобы сохранить график
```bash
cd utils
python plot_losses.py parsed_logs.json loss_plot.png
```