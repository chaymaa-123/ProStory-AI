'use client'

import { Card } from '@/components/ui/card'
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts'

interface TrendDataPoint {
  date: string
  positive: number
  neutral: number
  negative: number
}

interface TrendChartProps {
  data: TrendDataPoint[]
  title?: string
  period?: string
}

export function TrendChart({
  data,
  title = 'Perception Trend',
  period = '30 Days',
}: TrendChartProps) {
  return (
    <Card className="p-6">
      <div className="mb-6">
        <h3 className="font-semibold text-lg text-foreground">
          {title}
        </h3>
        <p className="text-sm text-muted-foreground">
          Last {period}
        </p>
      </div>

      <div className="h-80">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart
            data={data}
            margin={{ top: 5, right: 30, left: 0, bottom: 5 }}
          >
            <CartesianGrid
              strokeDasharray="3 3"
              stroke="oklch(0.9 0.01 265)"
            />
            <XAxis
              dataKey="date"
              stroke="oklch(0.48 0.02 265)"
              style={{ fontSize: '12px' }}
            />
            <YAxis
              stroke="oklch(0.48 0.02 265)"
              style={{ fontSize: '12px' }}
            />
            <Tooltip
              contentStyle={{
                backgroundColor: 'oklch(1 0 0)',
                border: '1px solid oklch(0.9 0.01 265)',
                borderRadius: '8px',
              }}
              labelStyle={{ color: 'oklch(0.18 0.02 265)' }}
            />
            <Legend
              wrapperStyle={{ paddingTop: '20px' }}
              iconType="line"
            />
            <Line
              type="monotone"
              dataKey="positive"
              stroke="oklch(0.65 0.12 150)"
              strokeWidth={2}
              dot={false}
              name="Positive"
            />
            <Line
              type="monotone"
              dataKey="neutral"
              stroke="oklch(0.94 0.01 265)"
              strokeWidth={2}
              dot={false}
              name="Neutral"
            />
            <Line
              type="monotone"
              dataKey="negative"
              stroke="oklch(0.63 0.18 25)"
              strokeWidth={2}
              dot={false}
              name="Negative"
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </Card>
  )
}
